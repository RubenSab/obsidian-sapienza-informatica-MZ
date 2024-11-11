file = open('../../../Obsidian/BRAIN/tabella.md', 'w')


class table:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    def __str__(self):
        return ('| head '*self.columns) + '|\n' + '| --- '*self.columns + '|\n' + ('| val '*self.columns+'|\n')*self.rows


t = table(5, 6)
file.write(str(t))
file.close()
