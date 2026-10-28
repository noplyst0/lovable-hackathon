#!/bin/bash
# PUT one file to a presigned Lovable upload URL from get_file_upload_url.
# Usage: build/put_upload.sh <file> '<upload url>' '<x-goog-meta-user_id>'
# Then pass the returned file_id in create_project / send_message `files`.
# URLs expire after 1 hour and land in "ephemeral" storage: upload right before the prompt.
set -euo pipefail
file="$1"; url="$2"; uid="$3"
case "$file" in
  *.png) type=image/png ;;
  *.jpg|*.jpeg) type=image/jpeg ;;
  *) type=application/octet-stream ;;
esac
code=$(curl -s -o /dev/null -w "%{http_code}" -X PUT \
  -H "Content-Type: $type" \
  -H "x-goog-content-length-range: 0,262144000" \
  -H "x-goog-meta-user_id: $uid" \
  --data-binary @"$file" "$url")
echo "$code $file"
[ "$code" = 200 ]
