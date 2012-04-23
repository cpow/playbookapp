# Contains class Playbook which is made up of plays.  Each play is made up of images with positions.
class Playbook:
    play_list=[]
    name=""
    def add_play(self, play):
        self.play_list.append(play)
    def __str__(self):
        retstring=""
        for play in self.play_list[:]:
            retstring+=str(play)+"\n"
        return retstring

class Play:
    img_list = []
    def add_img(self, img):
        self.img_list.append(img)
    def __str__(self):
        retstring=""
        for img in self.img_list[:]:
            retstring+=str(img)+"\n"
        return retstring


class Img:
    def __init__(self, imgloc, left, top):
        self.loc = imgloc
        self.left = left
        self.top = top
    def __str__(self):
        return "<img src='" + self.loc + "' style=\"position: relative; top: " + self.top + ";  left:" + self.left + ";\">"

if __name__ == '__main__':
    img1 = Img("/home/scorriere/blah.img", "30", "100")
    img2 = Img("/home/scorriere/blah2.img", "0", "100")
    testplay = Play()
    testplay.add_img(img1)
    testplay.add_img(img2)
    print testplay
    pb= Playbook()
    pb.add_play(testplay)
    print pb
