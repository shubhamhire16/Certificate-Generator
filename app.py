import cv2

list_of_names = []


def cleanup_data():
    with open("name-list-data.txt") as file:
        for line in file:
            list_of_names.append(line.strip())


def generate_certificate():
    for index, name in enumerate(list_of_names):
        template = cv2.imread("certificate-template.jpg")
        cv2.putText(template, name, (821,1437), cv2.FONT_HERSHEY_SIMPLEX, 5, (56, 7, 20),5,cv2.LINE_AA)
        cv2.imwrite(f'generated-certificate-data/{name}.jpg',template)
        print(f'Processing {index+1} / {len(list_of_names)}')

cleanup_data()
generate_certificate()