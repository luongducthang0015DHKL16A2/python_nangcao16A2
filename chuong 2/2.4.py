'''luong duc thang'''
import xml.dom.minidom

def main():
      doc=xml.dom.minidom.parse("sample.xml")
      print(doc.nodeName)
      print(doc.firstChild.tagName)
      
      name_staff= doc.getElementsByTagName('staff')
      
      print('%d staff'%name_staff.length)
      for staff in name_staff :
            name=staff.getElementsByTagName('name')[0].firstChild.nodeValue
            salary=staff.getElementsByTagName('salary')[0].firstChild.nodeValue
            print(f'Name: {name}; Salary: {salary}')
                        
if __name__=="__main__":
      main()
      