python ./tools/train_net.py \
    --dataset_name          diccio_layout \
    --json_annotation_train train.json \
    --image_path_train      ./training_imagenes/\
    --json_annotation_val   test.json \
    --image_path_val        ./training_imagenes/ \
    --config-file           ./configs/prima/fast_rcnn_R_50_FPN_3x.yaml \
    OUTPUT_DIR  ./outputs/fast_rcnn_R_50_FPN_3x/ \
    SOLVER.IMS_PER_BATCH 2