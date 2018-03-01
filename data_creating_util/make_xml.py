import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os

# add a tag that is not first one
def add_normal_tag(parent_tag, tag_name, tag_text):
    added_tag = ET.SubElement(parent_tag, tag_name)
    added_tag.text = tag_text


f = open('kitkat512')
# annotation用のXMLファイルが置かれるディレクトリ
os.makedirs('./kitkat_images2/annotation', exist_ok=True)

lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)

for line in lines:
    backslash_splitted_line = line.split("/")
    print('backslash', backslash_splitted_line)
    space_splitted_line = backslash_splitted_line[3].split(" ")
    image_name = space_splitted_line.pop(0)
    loop_count = int(space_splitted_line.pop(0))
    print(image_name)
    # first tag
    annotation = ET.Element('annotation')
    add_normal_tag(annotation, 'folder', 'training_set')
    # folder = ET.SubElement(annotation, 'folder')
    # folder.text = 'training_set'
    add_normal_tag(annotation, 'filename', image_name)
    # filename = ET.SubElement(annotation, 'filename')
    # filename.text = image_name
    # source
    source = ET.SubElement(annotation, 'source')
    add_normal_tag(source, 'database', 'tomita_kazuya')
    # database = ET.SubElement(source, 'database')
    # database.text = 'tomita_kazuya'
    #
    # owner
    owner = ET.SubElement(annotation, 'owner')
    add_normal_tag(owner, 'name', 'tomita_kazuya')
    # name = ET.SubElement(owner, 'owner')
    # name.text = 'tomita_kazuya'
    # size
    size = ET.SubElement(annotation, 'size')
    add_normal_tag(size, 'width', str(300))
    add_normal_tag(size, 'height', str(300))
    add_normal_tag(size, 'depth', str(3))
    # width_tag = ET.SubElement(size, 'width')
    # width_tag.text = 300
    # height_tag = ET.SubElement(size, 'height')
    # height_tag.text = 300
    # depth = ET.SubElement(size, 'depth')
    # depth.text = 3
    add_normal_tag(annotation, 'segmented', str(1))
    # segmented = ET.SubElement(annotation, 'segmented')
    # segmented.text = 1





    # from_image_name_to_data = [data for data in line[15:20]]

    for i in range(0, loop_count):
        object = ET.SubElement(annotation, 'object')
        add_normal_tag(object, 'name', 'kitkat')
        # name = ET.SubElement(object, 'name')
        # name.text = 'kitkat'
        add_normal_tag(object, 'pose', 'Unspecified')
        # pose = ET.SubElement(object, 'pose')
        # pose.text
        add_normal_tag(object, 'truncated', str(0))
        add_normal_tag(object, 'difficult', str(0))

        bounding_box = ET.SubElement(object, 'bndbox')

        x = space_splitted_line[0 + i * 4]
        y = space_splitted_line[1 + i * 4]
        width = space_splitted_line[2 + i * 4]
        height = space_splitted_line[3 + i * 4]
        print(x, y, width, height)

        add_normal_tag(bounding_box, 'xmin', x)
        add_normal_tag(bounding_box, 'ymin', y)
        add_normal_tag(bounding_box, 'xmax', str(int(x) + int(width)))
        add_normal_tag(bounding_box, 'ymax', str(int(y) + int(height)))

    # with open(image_name + '.xml', 'w+') as new_file:
    #     new_file.write(annotation)
    # tree = ET.ElementTree(element=annotation)
    # tree.write(image_name + '.xml', encoding='utf-8', xml_declaration=True)
    string = ET.tostring(annotation, 'utf-8')
    pretty_string = minidom.parseString(string).toprettyxml(indent='  ')

    with open('./kitkat_images2/annotation/' + image_name + '.xml', 'w+') as new_file:
        new_file.write(pretty_string)
f.close()
