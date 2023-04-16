import sys

def main():

    templ = '''---
weight: {}
---
'''
    numbers = {
        'man-fluxbox.md': 1,
        'man-startfluxbox.md': 2,
        'man-fluxbox-keys.md': 3,
        'man-fluxbox-apps.md': 4,
        'man-client-patterns.md': 5,
        'man-fluxbox-menu.md': 6,
        'man-fluxbox-style.md': 7,
        'man-fluxbox-fbsetbg.md': 8,
        'man-fluxbox-fbsetroot.md': 9,
        'man-fluxbox-fbrun.md': 10,
        'man-fluxbox-remote.md': 11,
    }

    id = sys.argv[1]

    if id in numbers:
        print(templ.format(numbers[id]))
    sys.stdout.write(sys.stdin.read())

if __name__ == "__main__":
    main()
