DOC=slidesShort
echo processing $DOC ...
pandoc -t dzslides -s $DOC.md -o $DOC.html || exit 1
DOC=${DOC}_comment
echo processing $DOC ...
pandoc -t dzslides -s $DOC.md -o $DOC.html || exit 1
patch slidesShort.html < styleOK.patch
