from PIL import Image

def c(a):
    return (a + 1) % 256

def s(coord, n, dim, sign):
    return (coord + sign * (dim // (n + 1))) % dim 

rounds = 4
for n in range(rounds):
    i = Image.open(str(n)+'.jpg')
    p = i.load()
    img = Image.new(i.mode, i.size)
    i.close()
    p_new = img.load()
    h = img.size[1]
    w = img.size[0]
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            up, down, left, right = p[s(x, n, w, -1), y], p[s(x, n, w, 1), y],\
                                    p[x, s(y, n, h, -1)], p[x, s(y, n, h, 1)]
            r_n = up[0] + down[0] + left[0] + right[0]
            g_n = up[1] + down[1] + left[1] + right[1] 
            b_n = up[2] + down[2] + left[2] + right[2]
            p_new[x, y] = (c(r_n), c(g_n),  c(b_n))
    img.save(str(n + 1) + '.jpg')
    img.close()
print('done')
