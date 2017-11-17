#! /usr/bin/python
import feedparser
import os
os.system('clear')


page = feedparser.parse("https://www.reddit.com/r/GifRecipes/.rss")

def gifrecipe_finder():
    os.system('clear')
    word = raw_input('\n What do you wanna cook? ')
    search_term_found = False
    for i in page.entries:
        if word in i.title or word in i.link:
            print '\n'
            print ' ' + i.title
            print ' ' + i.link
            print '\n'
            search_term_found = True

    if not search_term_found:
        print '\n No {} recipes yet, I\'m afraid \n'.format(word)

    # Ask if user wants to continue.
    do_over()



def do_over():
    again = raw_input('\n Still hungry?(y/n) ')
    while again not in ('y', 'n'):
        again_two = raw_input('\n Sorry, didn\'t catch that.(y/n) ')
        if again_two == 'y':
            gifrecipe_finder()
        elif again_two == 'n':
                quit()
    if again == 'y':
        gifrecipe_finder()
    elif again == 'n':
            quit()





gifrecipe_finder()


# Problems breakdown:

# make the else statement pop up only when there is NO recipe with said keyword
