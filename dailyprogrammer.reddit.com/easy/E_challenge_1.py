def main():
    name = input('Your name please? ').strip()
    age = int(input('Your age please: ').strip())
    reddit = input('Your reddit username please: ').strip()
    print('your name is {}, you are {} years old, and your username is {}'.format(name, age, reddit))
    #bonus
    #import os
    filename = os.path.abspath(os.path.join('.', 'data', 'reddituser.log'))
    how = 'w'
    if os.path.exists(filename):
        how = 'a'
    with open(filename, how) as fout:
        fout.write('{}|{}|{}\n'.format(name, age, reddit))
    print('reddituser.log updated!')
