echo '$1 -> $2(.jpeg)'
convert -resize 480x640! $1 resize_$2
mv $1 finish.jpeg

