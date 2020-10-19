convert sup5.jpg 16.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" res_chk.jpg
