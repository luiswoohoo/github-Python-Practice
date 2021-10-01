text = input()
text_reversed = ''
quit = {'Done', 'done', 'd'}

while text not in quit:
    for char in reversed(text):
        text_reversed += char

    print(text_reversed)
    text_reversed = ''

    text = input()

