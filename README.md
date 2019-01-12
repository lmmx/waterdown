# waterdown

Remove image watermarks with numpy

## Project goals

- [ ] Use numpy to detect and reproduce the original watermark (produce output from which to load for future use)
- [ ] Inpaint/offset the watermark region so as to unmark the image
- [x] Calculate the alpha opacity of the watermark
  - 24/255, or around 9.4%
- [ ] Apply to a gif (of a different size to the still images)

## Example usage (interactive)

So far all I've done is obtain some still/animated images (from
_Kirby Of The Stars_) and to focus on the watermark region in question.

The file `kirby003_01a.png` can be used to extract the binary watermark,
since it falls in a region of black screen fill.

```py
img = read_image('kirby003_01a.png')
watered = img[6:20, 9:109]
bin_wm = rgb2grey(watered)
```

The values in `bin_wm` are a binary (i.e. greyscale only) equivalent to
the RGB(A) values given by `imageio.imread` (equivalent to a numpy array).

An example value can be shown to be simply a decimal interpretation of RGB:

- `watered[10,10]` ⇒ `Array([ 24,  24,  24, 255], dtype=uint8)`
- `bin_wm[10,10]` ⇒ `0.09411764705882353`
- `24/255` ⇒ `0.09411764705882353`
```

Watermark removal should then just be a matter of offsetting the value stored
above in the variable `watered`...
