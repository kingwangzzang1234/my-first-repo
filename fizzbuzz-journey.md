vagrant@ubuntu:~/Documents/dev/my-first-repo$ touch fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ ls
LICENSE  README.md  fizzbuzz.py  hello.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ vi fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ cat fizzbuzz.py
def do_fizzbuzz():
	for i in range(1,15+1):
		if i%3==0:
			print('fizz')
		elif i%5==0:
			print('buzz')
		else:
			print(f'{i}')


if __name__=='__main__':
	do_fizzbuzz()
vagrant@ubuntu:~/Documents/dev/my-first-repo$ python fizzbuzz.py
1
2
fizz
4
  1 def do_fizzbuzz():
  2     for i in range(1,15+1):
  3         if i%3==0:
  4             print('fizz')
  5         elif i%5==0:
  6             print('buzz')
  7         else:
  8             print(f'{i}')
  9
 10
 11 if __name__=='__main__':
 12     do_fizzbuzz()
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"fizzbuzz.py" 12L, 173B                                                                          1,1           All
  1 def do_fizzbuzz():
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	fizzbuzz.py

nothing added to commit but untracked files present (use "git add" to track)
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git add fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git commit -m "feat: Print fizz or buzz
>
> Print fizz if i is multiple of 3.
> Print buzz if i is multiple of 5.
> Otherwise, print i itself."
[main 39c2c0d] feat: Print fizz or buzz
 1 file changed, 12 insertions(+)
 create mode 100644 fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ vi fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ python fizzbuzz.py
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz
vagrant@ubuntu:~/Documents/dev/my-first-repo$ cat fizzbuzz.py
def do_fizzbuzz():
	for i in range(1,15+1):
		if i%3==0:
			print('fizz')
		elif i%5==0:
			print('buzz')
		elif i%15==0:
			print('fizzbuzz')
		else:
			print(f'{i}')


if __name__=='__main__':
	do_fizzbuzz()
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git add fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git commit -m "feat: Print fizzbuzz
> Print fizzbuzz if i is multiple of 15."
[main 3b84688] feat: Print fizzbuzz Print fizzbuzz if i is multiple of 15.
 1 file changed, 2 insertions(+)
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git blame
usage: git blame [<options>] [<rev-opts>] [<rev>] [--] <file>

    <rev-opts> are documented in git-rev-list(1)

    --incremental         show blame entries as we find them, incrementally
    -b                    do not show object names of boundary commits (Default: off)
    --root                do not treat root commits as boundaries (Default: off)
    --show-stats          show work cost statistics
    --progress            force progress reporting
    --score-debug         show output score for blame entries
    -f, --show-name       show original filename (Default: auto)
    -n, --show-number     show original linenumber (Default: off)
    -p, --porcelain       show in a format designed for machine consumption
    --line-porcelain      show porcelain format with per-line commit information
    -c                    use the same output mode as git-annotate (Default: off)
    -t                    show raw timestamp (Default: off)
    -l                    show long commit SHA1 (Default: off)
    -s                    suppress author name and timestamp (Default: off)
  1 def do_fizzbuzz():
  2     for i in range(1,15+1):
  3         if i%3==0:
  4             print('fizz')
  5         elif i%5==0:
  6             print('buzz')
  7         elif i%15==0:
  8             print('fizzbuzz')
  9         else:
 10             print(f'{i}')
 11
 12
 13 if __name__=='__main__':
 14     do_fizzbuzz()
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"fizzbuzz.py" 14L, 210B                                                                          1,1           All
  1 def do_fizzbuzz():
    -e, --show-email      show author email instead of name (Default: off)
    -w                    ignore whitespace differences
    --ignore-rev <rev>    ignore <rev> when blaming
    --ignore-revs-file <file>
                          ignore revisions from <file>
    --color-lines         color redundant metadata from previous line differently
    --color-by-age        color lines by age
    --minimal             spend extra cycles to find better match
    -S <file>             use revisions from <file> instead of calling git-rev-list
    --contents <file>     use <file>'s contents as the final image
    -C[<score>]           find line copies within and across files
    -M[<score>]           find line movements within and across files
    -L <range>            process only line range <start>,<end> or function :<funcname>
    --abbrev[=<n>]        use <n> digits to display object names

vagrant@ubuntu:~/Documents/dev/my-first-repo$ git blame fizzbuzz.py
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  1) def do_fizzbuzz():
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  2) 	for i in range(1,15+1):
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  3) 		if i%3==0:
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  4) 			print('fizz')
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  5) 		elif i%5==0:
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  6) 			print('buzz')
3b84688b (kingwangzzang1234 2024-01-12 07:36:07 +0000  7) 		elif i%15==0:
3b84688b (kingwangzzang1234 2024-01-12 07:36:07 +0000  8) 			print('fizzbuzz')
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000  9) 		else:
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000 10) 			print(f'{i}')
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000 11)
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000 12)
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000 13) if __name__=='__main__':
39c2c0d7 (kingwangzzang1234 2024-01-12 07:31:15 +0000 14) 	do_fizzbuzz()
vagrant@ubuntu:~/Documents/dev/my-first-repo$ vi fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ python fizzbuzz.py
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
vagrant@ubuntu:~/Documents/dev/my-first-repo$ cat fizzbuzz.py
def do_fizzbuzz():
	for i in range(1,15+1):
  1 def do_fizzbuzz():
  2     for i in range(1,15+1):
  3         if i%15==0:
  4             print('fizzbuzz')
  5         elif i%3==0:
  6             print('fizz')
  7         elif i%5==0:
  8             print('buzz')
  9         else:
 10             print(f'{i}')
 11
 12
 13 if __name__=='__main__':
 14     do_fizzbuzz()
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"fizzbuzz.py" 14L, 210B                                                                          1,1           All
  1 def do_fizzbuzz():
		if i%15==0:
			print('fizzbuzz')
		elif i%3==0:
			print('fizz')
		elif i%5==0:
			print('buzz')
		else:
			print(f'{i}')


if __name__=='__main__':
	do_fizzbuzz()
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git add fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git commit -m "fix: Adjust Priority"
[main 6864405] fix: Adjust Priority
 1 file changed, 3 insertions(+), 3 deletions(-)
vagrant@ubuntu:~/Documents/dev/my-first-repo$ def do_fizzbuzz():
        for i in range(1,15+1):
                if i%15==0:
                        print('fizzbuzz')
                elif i%3==0:
                        print('fizz')
                elif i%5==0:
                        print('buzz')
                else:
                        print(f'{i}')


if __name__=='__main__':
        do_fizzbuzz()^C
vagrant@ubuntu:~/Documents/dev/my-first-repo$ vi fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ python fizzbuzz.py
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
vagrant@ubuntu:~/Documents/dev/my-first-repo$ cat fizzbuzz.py
def do_fizzbuzz():
	for i in range(1,15+1):
		if i%3==0 or i%5==0:
			print('fizz'*(i%3==0)+'buzz'*(i%5==0))
		else:
			print(f'{i}')


if __name__=='__main__':
	do_fizzbuzz()
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git add fizzbuzz.py
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git commit -m "refactor: Do fizzbuzz with 1 if Statement"
[main 330353b] refactor: Do fizzbuzz with 1 if Statement
 1 file changed, 2 insertions(+), 6 deletions(-)
vagrant@ubuntu:~/Documents/dev/my-first-repo$ git push origin main
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 2 threads
Compressing objects: 100% (15/15), done.
Writing objects: 100% (15/15), 4.33 KiB | 2.17 MiB/s, done.
Total 15 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/kingwangzzang1234/my-first-repo.git
   f7f4564..330353b  main -> main
