document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
  const dropZoneElement = inputElement.closest(".drop-zone");

  inputElement.addEventListener("change", (e) => {
    const files = inputElement.files;
    if (files.length > 0) {
      updateFileCount(dropZoneElement, files.length);
    }
  });

  ["dragover", "dragleave", "dragend", "drop"].forEach((type) => {
    dropZoneElement.addEventListener(type, (e) => {
      e.preventDefault();

      if (type === "drop" && e.dataTransfer.files.length > 0) {
        const files = e.dataTransfer.files;
        // Use the DataTransfer object to update the input files
        inputElement.files = files;
        updateFileCount(dropZoneElement, files.length);
      }

      dropZoneElement.classList.remove("drop-zone--over");
    });
  });

  // Add a click event to trigger the file input when clicking on the drop zone
  dropZoneElement.addEventListener("click", () => {
    inputElement.click();
  });
});

function updateFileCount(dropZoneElement, count) {
  let fileCountElement = dropZoneElement.querySelector(
    ".drop-zone__file-count"
  );

  if (!fileCountElement) {
    fileCountElement = document.createElement("div");
    fileCountElement.classList.add("drop-zone__file-count");
    dropZoneElement.appendChild(fileCountElement);
  }

  fileCountElement.textContent =
    count === 1 ? `${count} file uploaded` : `${count} files uploaded`;

  dropZoneElement
    .querySelectorAll(".drop-zone__thumb")
    .forEach((thumbElement) => {
      thumbElement.remove();
    });

  dropZoneElement.querySelector(".drop-zone__prompt")?.remove();
}
