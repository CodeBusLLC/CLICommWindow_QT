import yaml

class LoadData_Yaml():
  def __init__(self, aOwner, aFile):
    with open(aFile, 'r') as file:
      ydata_ = yaml.full_load(file)
      #print(ydata_)
      print(ydata_['Version'])
      #aOwner.versions.append( aFile + ' ' + ydata_['Version'] )
      for category_ in ydata_['Categories']:
        #print(category_['name'])
        categoryValue_ = category_['value']
#        parent_ = tv.insert('', "end", text="", values=(category_['name'], "", "", category_['help']), open=True)
        parent_ = aOwner.addTop( "", (category_['name'], "", "", category_['help']) )
        for element_ in category_['Elements']:
          #print(element_)
          #print( "%s %s" % (element_['name'], element_['value']) )
          help_ = ''
          if 'Help' in element_:
            help_ = element_['Help']
#          tv.insert(parent_, "end", text="%s %s" % (categoryValue_, element_['value']), values=("", "", element_['name'], help_), open=True)
          aOwner.addChild( parent_, "%s %s" % (categoryValue_, element_['value']), ("", "", element_['name'], help_) )
        if 'Group' in category_:
          for group_ in category_['Group']:
            help_ = ''
            if 'Help' in group_:
              help_ = group_['Help']
            #parent1_ = tv.insert(parent_, "end", text="", values=("", group_['name'], "", help_), open=True)
            parent1_ = aOwner.addChild( parent_, "", ("", group_['name'], "", help_) )
            for element_ in group_['Elements']:
              #print(element_)
            #print( "%s %s" % (element_['name'], element_['value']) )
              help_ = ''
              if 'Help' in element_:
                help_ = element_['Help']
              #tv.insert(parent1_, "end", text="%s %s" % (categoryValue_, element_['value']), values=("", "", element_['name'], help_), open=True)
              aOwner.addChild( parent1_, "%s %s" % (categoryValue_, element_['value']), ("", "", element_['name'], help_) )

