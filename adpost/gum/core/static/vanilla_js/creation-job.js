const uploadButton = document.querySelector('#add');
const deleteButton = document.querySelector('#delete');
const inputFile = document.querySelector('input[type="file"]');
const logoContainer = document.querySelector('.logo-container');

uploadButton.addEventListener('click', function () {
    inputFile.click();
});

inputFile.addEventListener('change', function () {
    const file = inputFile.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imgSrc = e.target.result;
            logoContainer.innerHTML = `<img src="${imgSrc}" alt="Uploaded Image">`;
            logoContainer.style.display = 'block';
            deleteButton.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

deleteButton.addEventListener('click', function () {
    logoContainer.innerHTML = '';
    logoContainer.style.display = 'none';
    deleteButton.style.display = 'none';
    inputFile.value = ''; // Clear the input file to remove the uploaded image.
});
