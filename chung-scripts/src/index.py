from util import generate_image, generate_next_index

next_index = generate_next_index()

prompt = 'face lighting,bright backlight,medium breasts,super high resolution,best quality,Photos,4k,(Realistic:1.2),(knolling:1.2),1girl,shoes,nipples,solo,breasts,sneakers,(nude:1.4),long hair,jacket,(shoes removed:1.2),shorts,navel,lying,looking at viewer,pussy,full body,gym shorts,shirt,(completely nude:1.2),red jacket,barefoot,wooden floor,medium breasts,clothes removed,gun,from above,short shorts,sportswear,gym uniform,underwear,(arrange clothes neatly:1.7),bag,track jacket, <lora:knolling_20230726093614:0.7>,chill_mayuki,<lora:chill_mayuki:0.3>,mix4,<lora:mix4:0.5>,'
generate_image(prompt, next_index)

