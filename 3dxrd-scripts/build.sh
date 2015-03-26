mkdir -p $PREFIX/bin
cp -r $RECIPE_DIR/findpeaks $PREFIX/bin/
cp -r $RECIPE_DIR/makemap_all $PREFIX/bin/
cp -r $RECIPE_DIR/grainspotter_loop $PREFIX/bin/
cp -r $RECIPE_DIR/tweakdetpars $PREFIX/bin/
cp -r $RECIPE_DIR/filter_images $PREFIX/bin/
cp -r $RECIPE_DIR/ge2tiff $PREFIX/bin/
cp -r $RECIPE_DIR/stack_layers $PREFIX/bin/

mkdir -p $PREFIX/share/3dxrd
cp $RECIPE_DIR/*.ini $PREFIX/share/3dxrd/
