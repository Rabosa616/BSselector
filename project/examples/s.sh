pandoc -t dzslides -s slidesShort.md -o slidesShort.html
patch slidesShort.html < styleOK.patch
