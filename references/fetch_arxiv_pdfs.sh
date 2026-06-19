#!/usr/bin/env bash
# Pobiera brakujace PDF-y cytowanych prac z arXiv (sekcja A z TODO_download.md).
# Pelne naglowki przegladarki (arXiv odrzuca "gole" curl) + usuwanie CR (pliki maja CRLF).
# Wznawialny: pomija to, co juz jest. Uruchom z dowolnej sieci docelowej:
#   bash fetch_arxiv_pdfs.sh
#   SLEEP=2 bash fetch_arxiv_pdfs.sh   # odstep miedzy pobraniami (domyslnie 2 s)

cd "$(dirname "$0")" || exit 1
SLEEP="${SLEEP:-2}"
H=(
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
  -H 'accept-language: en-US,en;q=0.9'
  -H 'sec-ch-ua: "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"'
  -H 'sec-ch-ua-mobile: ?0'
  -H 'sec-ch-ua-platform: "Windows"'
  -H 'sec-fetch-dest: document'
  -H 'sec-fetch-mode: navigate'
  -H 'sec-fetch-site: none'
  -H 'sec-fetch-user: ?1'
  -H 'upgrade-insecure-requests: 1'
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
)
valid() { [ -s "$1" ] && head -c4 "$1" | grep -q "%PDF"; }
ok=0; fail=0; failed=""
while IFS=$'\t' read -r key id; do
  key="${key%$'\r'}"; id="${id%$'\r'}"          # usun CR (Windows CRLF)
  [ -z "$key" ] && continue
  f="cited/$key/paper.pdf"; mkdir -p "cited/$key"
  if valid "$f"; then ok=$((ok+1)); continue; fi
  curl -fsSL "${H[@]}" --max-time 120 -o "$f" "https://arxiv.org/pdf/$id" 2>/dev/null
  if valid "$f"; then ok=$((ok+1)); echo "OK   $key  ($(du -h "$f" | cut -f1))"
  else fail=$((fail+1)); failed="$failed $key"; echo "FAIL $key ($id)"; rm -f "$f"; fi
  sleep "$SLEEP"
done < arxiv_list.tsv
echo "=== Gotowe: OK=$ok FAIL=$fail. PDF w cited/: $(find cited -name paper.pdf | wc -l) ==="
[ -n "$failed" ] && echo "Nieudane (uruchom ponownie):$failed"
