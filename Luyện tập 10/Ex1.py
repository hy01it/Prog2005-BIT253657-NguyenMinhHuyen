    def get_filename(path):
        return path.split("\\")[-1]
    def get_name(path):
        filename = get_filename(path)
        return filename.split(".")[0]
    path = "d:\\music\\muabui.mp3"
    print("Tên file:", get_filename(path))
    print("Tên bài:", get_name(path))
