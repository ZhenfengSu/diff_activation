for i in {0..11}; do  
  echo $i  
  python main.py --eval --resume ./ckpt/deit_small_patch16_224-cd65a155.pth --data-path /root/autodl-tmp/yy/imagenet --model deit_small_patch16_224  --dist-eval --eval --output_dir ./output_small --target_id $i
  # python main.py --eval --resume ./ckpt/deit_tiny_patch16_224-a1311bcf.pth --data-path /root/autodl-tmp/yy/imagenet --model deit_tiny_patch16_224  --dist-eval --eval --output_dir ./output_dir --target_id $i
done
# python main.py --eval --resume ./ckpt/deit_tiny_patch16_224-a1311bcf.pth --data-path /root/autodl-tmp/yy/imagenet --model deit_tiny_patch16_224 --batch-size 128 --dist-eval --eval --output_dir ./output_dir