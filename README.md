# waterdown

Remove image watermarks with numpy

## Project goals

- Use numpy to detect and reproduce the original watermark (produce output from which to load for future use)
- Inpaint/offset the watermark region so as to unmark the image

## Potential stretch goals

- Calculate the alpha opacity of the watermark
- Apply to a gif (of a different size to the still images)

## Example usage (interactive)

So far all I've done is to focus on the watermark region in question:

```py
img = read_image('kirby001_01.png')
img2 = read_image('kirby001_02.png')
wm = get_wm(img)
wm2 = get_wm(img2)
```
