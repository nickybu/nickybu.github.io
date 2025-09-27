for file in content/**/*.md; do
  if ! grep -q '^date:' "$file"; then
    cdate=$(stat -c %w "$file" | cut -d' ' -f1)
    [ "$cdate" = "-" ] && cdate=$(stat -c %y "$file" | cut -d' ' -f1)
    sed -i "1s/^/date: $cdate\n/" "$file"
  fi
done