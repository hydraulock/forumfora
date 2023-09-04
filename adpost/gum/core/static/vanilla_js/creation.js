const uploadButton = document.querySelector('#add');
    const inputFile = document.querySelector('input[type="file"]');
    const imagesContainer = document.getElementById('images-container');

    // Counter to keep track of the image position
    let imageCounter = 1;

    // Store uploaded images in an array
    const imageArray = [];

    // Function to delete an image from the array and update the display
    function deleteImage(index) {
        imageArray.splice(index, 1);
        displayImages();
    }

    // Function to display all images in the container
    function displayImages() {
        imagesContainer.innerHTML = '';

        imageArray.forEach((image, index) => {
            const imageWrapper = document.createElement('div');
            imageWrapper.className = 'col-md-3 col-6 border d-flex align-items-center position-relative image-uploaded';

            const img = document.createElement('img');
            img.className = 'w-100 h-75 object-fit-contain';
            img.src = URL.createObjectURL(image);
            img.alt = 'Uploaded Image';

            const deleteBtn = document.createElement('span');
            deleteBtn.id = 'delete-btn';
            deleteBtn.className = 'position-absolute';
            deleteBtn.innerHTML = '<i class="fa-solid fa-circle-minus"></i>';
            deleteBtn.addEventListener('click', () => deleteImage(index));

            imageWrapper.appendChild(deleteBtn);
            imageWrapper.appendChild(img);
            imagesContainer.appendChild(imageWrapper);
        });
    }

    // Function to handle file input changes
    function handleFileInput() {
        const files = inputFile.files;

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            // Check if it's an image file (you may add additional checks based on file type if needed)
            if (file.type.startsWith('image/')) {
                // Assign the file input name based on the image position
                file.name = `product_image${imageCounter}`;
                imageCounter++;
                imageArray.push(file);
            }
        }

        displayImages();
    }

    uploadButton.addEventListener('click', function () {
        inputFile.click();
    });

    inputFile.addEventListener('change', handleFileInput);