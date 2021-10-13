import csv

import numpy as np
from PIL import Image
from torch.utils.data import Dataset

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

class AttributesDataset():
    def __init__(self, annotation_path):
        Tipo_labels = []
        Dano_labels = []
        Tamano_labels = []

        with open(annotation_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                Tipo_labels.append(row['Tipo'])
                Dano_labels.append(row['Dano'])
                Tamano_labels.append(row['Tamano'])

        self.Tipo_labels = np.unique(Tipo_labels)
        self.Dano_labels = np.unique(Dano_labels)
        self.Tamano_labels = np.unique(Tamano_labels)

        self.num_Tipo = len(self.Tipo_labels)
        self.num_Dano = len(self.Dano_labels)
        self.num_Tamano = len(self.Tamano_labels)

        self.Tipo_id_to_name = dict(zip(range(len(self.Tipo_labels)), self.Tipo_labels))
        self.Tipo_name_to_id = dict(zip(self.Tipo_labels, range(len(self.Tipo_labels))))

        self.Dano_id_to_name = dict(zip(range(len(self.Dano_labels)), self.Dano_labels))
        self.Dano_name_to_id = dict(zip(self.Dano_labels, range(len(self.Dano_labels))))

        self.Tamano_id_to_name = dict(zip(range(len(self.Tamano_labels)), self.Tamano_labels))
        self.Tamano_name_to_id = dict(zip(self.Tamano_labels, range(len(self.Tamano_labels))))


class PotatoDataset(Dataset):
    def __init__(self, annotation_path, attributes, transform=None):
        super().__init__()

        self.transform = transform
        self.attr = attributes

        # initialize the arrays to store the ground truth labels and paths to the images
        self.data = []
        self.Tipo_labels = []
        self.Dano_labels = []
        self.Tamano_labels = []

        # read the annotations from the CSV file
        with open(annotation_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data.append(row['image_path'])
                self.Tipo_labels.append(self.attr.Tipo_name_to_id[row['Tipo']])
                self.Dano_labels.append(self.attr.Dano_name_to_id[row['Dano']])
                self.Tamano_labels.append(self.attr.Tamano_name_to_id[row['Tamano']])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # take the data sample by its index
        img_path = self.data[idx]

        # read image
        img = Image.open(img_path)

        # apply the image augmentations if needed
        if self.transform:
            img = self.transform(img)

        # return the image and all the associated labels
        dict_data = {
            'img': img,
            'labels': {
                'Tipo_labels': self.Tipo_labels[idx],
                'Dano_labels': self.Dano_labels[idx],
                'Tamano_labels': self.Tamano_labels[idx]
            }
        }
        return dict_data