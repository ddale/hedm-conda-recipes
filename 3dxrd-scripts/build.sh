mkdir -p $PREFIX/bin
cp -r $RECIPE_DIR/findpeaks $PREFIX/bin/
cp -r $RECIPE_DIR/makemap_all $PREFIX/bin/
cp -r $RECIPE_DIR/grainspotter_loop $PREFIX/bin/
cp -r $RECIPE_DIR/tweakpars_*.py $PREFIX/bin/
cp -r $RECIPE_DIR/correct_*.py $PREFIX/bin/
cp -r $RECIPE_DIR/ge2tiff $PREFIX/bin/

mkdir -p $PREFIX/share/3dxrd
cp $RECIPE_DIR/*.ini $PREFIX/share/3dxrd/
