screen imagebutton_test():
  modal False
  vbox xalign 1.0 yalign 1.0:
    imagebutton:
      idle "screwdriver.png"
      action [SetVariable("screwdriver", True), Jump("screwdriver")]