mkdir -p $PREFIX/bin
cp -r $RECIPE_DIR/filter_images.py $PREFIX/bin/
cp -r $RECIPE_DIR/ge2tiff.py $PREFIX/bin/
cp -r $RECIPE_DIR/stack_layers.py $PREFIX/bin/

mkdir -p $PREFIX/share/3dxrd
cp $RECIPE_DIR/*.ini $PREFIX/share/3dxrd/
