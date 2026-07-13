const removeMemberModal = document.getElementById("removeMemberModal");

removeMemberModal.addEventListener("show.bs.modal", function (event) {

    const button = event.relatedTarget;

    const memberId = button.dataset.memberId;
    const memberName = button.dataset.memberName;

    document.getElementById("removeMemberTitle").textContent =
        `Remove ${memberName}?`;

    document.getElementById("removeMemberText").textContent =
        `Are you sure you want to remove ${memberName} from this campaign?`;

    const form = document.getElementById("removeMemberForm");

    const urlTemplate = form.dataset.urlTemplate;

    form.action = urlTemplate.replace("0", memberId);

});

const userFolders = document.querySelectorAll(".user-folder");

// Gendan tidligere åbne foldere
userFolders.forEach((folder) => {
    const isOpen = sessionStorage.getItem(folder.id);

    if (isOpen === "true") {
        folder.open = true;
    }

    folder.addEventListener("toggle", () => {
        sessionStorage.setItem(folder.id, folder.open);
    });
});