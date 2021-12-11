from guizero import *

def reduceTime():
    global timer
    if int(timer.value) > 0:
        timer.value = int(timer.value) - 1
    else:
        timer.value = "Time's Up!"

def startTimer(window):
    global timer
    pomWindow = Window(window, title="Timer")
    pomWindow.height = 100
    pomWindow.width = 250
    currentTimeLeft = 25
    timerTitle = Text(pomWindow, text="Timer")
    timer = Text(pomWindow, text=currentTimeLeft)
    timer.repeat(600, reduceTime)
    
def addActivity(activity):
    newActivity = ToDoWidget(activity, activityBox)

class ToDoWidget(object):
    def __init__(self, descr, window):
        self.__descr = descr
        self.__widgetSpace = Box(window)
        self.__widgetDecr = Text(self.__widgetSpace, text=self.__descr, align="left")
        self.__widgetDone = CheckBox(self.__widgetSpace, align="right")
        self.__widgetSpace.repeat(200, self.destroy_widget)

    def destroy_widget(self):
        try:
            if self.__widgetDone.value == 1:
                self.__widgetSpace.destroy()
        except:
            pass

    def remove_widget(self):
        if widgetDone.value == True:
            widgetSpace.destroy()

#App Creation    
app = App()

title = Text(app, text="Task Organizer")
pomodoroTimer = PushButton(app, text="Timer", command=lambda:startTimer(app))

entryBox = Box(app, align="top")
activityBox = Box(app, align="bottom")
activityBox.width=450
activityBox.height=500
activityBox.bg = "blue"

entryTxt = TextBox(entryBox, align="left")
entryTxt.width = 50
entryBtn = PushButton(entryBox, text="Add", command=lambda:addActivity(entryTxt.value), align="right")
app.display()