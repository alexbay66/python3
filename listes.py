text = "foo bar baz"
splitted_text = text.split('')

print(splitted_text)
print(len(splitted_text))
print(splitted_text[1])
print(splitted_text[2])
print(splitted_text[3])



my_text = "orem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate laoreet libero, sed aliquam ipsum congue ac. Quisque at dolor ultricies, fringilla nisi vel, elementum ligula. Cras vel mi in eros porta gravida quis non diam. Proin varius, mi vel vulputate vestibulum, tortor massa venenatis nisl, in ultrices nisi libero sed tortor. Ut nulla ante, eleifend vel aliquet at, tristique non ex. Proin posuere ligula ex, at aliquet dui elementum at. Donec dolor tortor, gravida non urna eu, accumsan faucibus purus. Fusce et dolor sodales, pellentesque mauris et, vestibulum ipsum. Sed finibus, leo ac egestas auctor, leo arcu placerat nisi, eu feugiat leo eros sed velit. Praesent eget ipsum non metus accumsan lobortis in in libero. Nam augue velit, egestas sed cursus dictum, consequat eget libero. Mauris vel neque non felis gravida tristique. Maecenas nulla mi, molestie quis orci vehicula, vestibulum dignissim nunc. Etiam lobortis feugiat aliquam. Maecenas molestie, velit sit amet pretium pharetra, ipsum magna tempor nulla, et dignissim ante dolor et orci. Aliquam erat volutpat."

splitted_my_tex = my_text.split(',')
my_text = '.'.join(splitted_my_tex)
print(my_text)