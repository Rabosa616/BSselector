DOC=twitch1
echo processing $DOC ...
pandoc -t dzslides -s $DOC.md -o $DOC.html || exit 1
patch $DOC.html < styleOK.patch

exit 0

DOC=slidesShort
echo processing $DOC ...
pandoc -t dzslides -s $DOC.md -o $DOC.html || exit 1
patch $DOC.html < styleOK.patch

#DOC=${DOC}_comment
DOC=slides
echo processing $DOC ...
pandoc -t dzslides -s $DOC.md -o $DOC.html || exit 1
patch $DOC.html < styleOK.patch
