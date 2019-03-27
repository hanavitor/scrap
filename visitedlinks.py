class VistedLinks:
    links = {}

    def __init__(self):
        table = []
        open("vlinklist.txt", 'a')
        with open("vlinklist.txt", 'r+') as f:
            table = f.readlines()
            for line in table:
                line = line.rstrip()
                self.links[line] = True

    def repeated_links(self, link):
        if self.links.get(link):
            return True
        else:
            return False

    def add_link(self, link):
        with open("vlinklist.txt", 'a') as f:
            f.write(link + "\n")
            self.links[link] = True
