import matplotlib.pyplot as plt

def class_switch(argument):
    # Classes 
    classes = ('Clase 1', 'Clase 2', 'Clase 3', 'Clase 4' ,'Clase 5' , 'Clase 6',
               'Clase 7', 'Clase 8', 'Clase 9', 'Clase 10','Clase 11', 'Clase 12')
    switcher = {
        1: classes[0],
        2: classes[1],
        3: classes[2],
        4: classes[3],
        5: classes[4],
        6: classes[5],
        7: classes[6],
        8: classes[7],
        9: classes[8],
        10: classes[9],
        11: classes[10],
        12: classes[11]
    }
    return switcher.get(argument, "Invalid class")

def visualize_gt_data(dataset, attributes):
    imgs = []
    gt_labels = []
    clases = []

    n_cols = 5
    n_rows = 3

    # store the original transforms from the dataset
    transforms = dataset.transform
    # and not use them during visualization
    dataset.transform = None

    for img_idx in range(n_cols * n_rows):
        sample = dataset[img_idx]
        img = sample['img']
        labels = sample['labels']
        gt_tipo = attributes.Tipo_id_to_name[labels['Tipo_labels']]
        gt_dano = attributes.Dano_id_to_name[labels['Dano_labels']]
        gt_tamano = attributes.Tamano_id_to_name[labels['Tamano_labels']]
        
        imgs.append(img)
        gt_labels.append("{}\n{}\n{}".format(gt_tipo, gt_dano, gt_tamano))

    for i in range(n_cols * n_rows):

      if gt_labels[i] == 'Pastusa\nBuena\nMediana':case = 1
      if gt_labels[i] == 'Pastusa\nBuena\nGrande' :case = 2
      if gt_labels[i] == 'Pastusa\nBuena\nMuy Grande' :case = 3
      if gt_labels[i] == 'Pastusa\nDefectuosa\nMediana':case = 4
      if gt_labels[i] == 'Pastusa\nDefectuosa\nGrande' :case = 5
      if gt_labels[i] == 'Pastusa\nDefectuosa\nMuy Grande' :case = 6
      if gt_labels[i] == 'R12\nBuena\nMediana':case = 7
      if gt_labels[i] == 'R12\nBuena\nGrande' :case = 8
      if gt_labels[i] == 'R12\nBuena\nMuy Grande' :case = 9
      if gt_labels[i] == 'R12\nDefectuosa\nMediana':case = 10
      if gt_labels[i] == 'R12\nDefectuosa\nGrande' :case = 11
      if gt_labels[i] == 'R12\nDefectuosa\nMuy Grande' :case = 12

      clases.append(class_switch(case))

	
    # IMAGE GRID
    title = "Ground truth labels"

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(10, 10))
    axs = axs.flatten()
    for img, ax, label, clases in zip(imgs, axs, gt_labels, clases):
        ax.set_xlabel(clases, rotation=0)
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.imshow(img)
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

    # restore original transforms
    dataset.transform = transforms