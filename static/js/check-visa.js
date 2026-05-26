let generatedCaptchaText = "";

/* =========================
   Generate Captcha
========================= */
function generateCaptcha() {
    const characters = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
    let result = "";

    for (let i = 0; i < 6; i++) {
        result += characters.charAt(
            Math.floor(Math.random() * characters.length)
        );
    }

    generatedCaptchaText = result;
    document.getElementById("captchaValue").textContent = result;
}

/* =========================
   Show Alert Modal (Error Only)
========================= */
function showAlert(title, message) {
    const overlay = document.getElementById("modalAlertOverlay");
    const titleElem = document.getElementById("modalAlertTitle");
    const messageElem = document.getElementById("modalAlertMessage");
    const successIcon = document.getElementById("modalIconSuccess");
    const errorIcon = document.getElementById("modalIconError");

    titleElem.textContent = title;
    messageElem.textContent = message;

    successIcon.style.display = "none";
    errorIcon.style.display = "block";

    overlay.classList.add("active");
}

/* =========================
   Close Modal
========================= */
function closeModal() {
    document
        .getElementById("modalAlertOverlay")
        .classList.remove("active");
}

/* =========================
   Main Logic
========================= */
window.addEventListener("DOMContentLoaded", function () {
    generateCaptcha();

    document
        .getElementById("btnRefreshCaptcha")
        .addEventListener("click", generateCaptcha);

    document
        .getElementById("btnModalClose")
        .addEventListener("click", closeModal);

    const visaForm = document.getElementById("visaForm");
    const visaSearchBlock = document.getElementById("visaSearchBlock");
    const visaResultContainer = document.getElementById("visaResultContainer");
    const visaNumberInput = document.getElementById("visaNumber");
    const visaNumberError = document.getElementById("visaNumberError");
    const verificationCodeInput = document.getElementById("verificationCode");
    const verificationCodeError = document.getElementById("verificationCodeError");

    function setVisaNumberValidity(isValid, message) {
        if (isValid) {
            visaNumberInput.classList.remove("invalid");
            visaNumberInput.classList.add("valid");
            visaNumberError.textContent = "";
            visaNumberError.classList.remove("visible");
            visaNumberInput.setAttribute("aria-invalid", "false");
        } else {
            visaNumberInput.classList.remove("valid");
            visaNumberInput.classList.add("invalid");
            visaNumberError.textContent = message;
            visaNumberError.classList.add("visible");
            visaNumberInput.setAttribute("aria-invalid", "true");
        }
    }

    function clearVisaNumberValidation() {
        visaNumberInput.classList.remove("invalid");
        visaNumberInput.classList.remove("valid");
        visaNumberError.textContent = "";
        visaNumberError.classList.remove("visible");
        visaNumberInput.setAttribute("aria-invalid", "false");
    }

    function setVerificationCodeValidity(isValid, message) {
        if (isValid) {
            verificationCodeInput.classList.remove("invalid");
            verificationCodeInput.classList.add("valid");
            verificationCodeError.textContent = "";
            verificationCodeError.classList.remove("visible");
            verificationCodeInput.setAttribute("aria-invalid", "false");
        } else {
            verificationCodeInput.classList.remove("valid");
            verificationCodeInput.classList.add("invalid");
            verificationCodeError.textContent = message;
            verificationCodeError.classList.add("visible");
            verificationCodeInput.setAttribute("aria-invalid", "true");
        }
    }

    function clearVerificationCodeValidation() {
        verificationCodeInput.classList.remove("invalid");
        verificationCodeInput.classList.remove("valid");
        verificationCodeError.textContent = "";
        verificationCodeError.classList.remove("visible");
        verificationCodeInput.setAttribute("aria-invalid", "false");
    }

    function validateVisaNumber() {
        const rawValue = visaNumberInput.value;
        const trimmedValue = rawValue.trim();
        const normalizedValue = trimmedValue.toUpperCase();
        visaNumberInput.value = normalizedValue;

        if (normalizedValue === "") {
            setVisaNumberValidity(false, "Please enter visa number");
            return false;
        }

        clearVisaNumberValidation();
        return true;
    }

    function validateVerificationCode() {
        const rawValue = verificationCodeInput.value;
        const trimmedValue = rawValue.trim();

        if (trimmedValue === "") {
            setVerificationCodeValidity(false, "Please enter verification code");
            return false;
        }

        if (trimmedValue.toUpperCase() !== generatedCaptchaText) {
            setVerificationCodeValidity(false, "Verification code does not match");
            return false;
        }

        clearVerificationCodeValidation();
        return true;
    }

    function toggleBlocks(showSearch) {
        if (showSearch) {
            visaSearchBlock.classList.remove("hidden-panel");
            visaSearchBlock.classList.add("visible-panel");
            visaResultContainer.classList.remove("visible-panel");
            visaResultContainer.classList.add("hidden-panel");
        } else {
            visaSearchBlock.classList.remove("visible-panel");
            visaSearchBlock.classList.add("hidden-panel");
            visaResultContainer.classList.remove("hidden-panel");
            visaResultContainer.classList.add("visible-panel");
        }
    }

    function resetSearchView() {
        toggleBlocks(true);
        visaNumberInput.value = "";
        verificationCodeInput.value = "";
        clearVisaNumberValidation();
        clearVerificationCodeValidation();
        visaResultContainer.innerHTML = "";
    }

    function renderVisaResult(visa) {
        const photoUrl = visa.photo_url || '/static/assets/person.jpg';

        visaResultContainer.innerHTML = `
            <div class="form-box">
                <div class="result-card-container">
                    <div class="result-card-table">
                        <div class="result-photo-cell">
                            <img src="${photoUrl}" class="applicant-photo" alt="Applicant photo">
                        </div>
                        <div class="result-info-cell">
                            <table class="info-grid">
                                <tr><td class="info-label">Surname:</td><td class="info-value">${visa.surname}</td></tr>
                                <tr><td class="info-label">First name:</td><td class="info-value">${visa.first_name}</td></tr>
                                <tr><td class="info-label">Date of birth:</td><td class="info-value">${visa.date_of_birth}</td></tr>
                                <tr><td class="info-label">Citizenship:</td><td class="info-value">${visa.citizenship}</td></tr>
                                <tr><td class="info-label">Passport number:</td><td class="info-value">${visa.passport_number}</td></tr>
                                <tr>
                                    <td colspan="2">
                                        <hr style="border:none; border-top:1px solid #b4c6c9; margin:5px 0;">
                                    </td>
                                </tr>
                                <tr>
                                    <td class="info-label">Visa status:</td>
                                    <td class="info-value">${visa.visa_status}</td>
                                </tr>
                                <tr>
                                    <td class="info-label">Visa validity:</td>
                                    <td class="info-value">${visa.visa_validity}</td>
                                </tr>
                                <tr>
                                    <td class="info-label">Visa type:</td>
                                    <td class="info-value">${visa.visa_type}</td>
                                </tr>
                                <tr>
                                    <td class="info-label">Visit purpose:</td>
                                    <td class="info-value">${visa.visit_purpose}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
                <div class="result-actions">
                    <button type="button" class="btn-another" id="btnAnotherSearch">Another Search</button>
                </div>
            </div>
        `;

        toggleBlocks(false);
        visaNumberInput.classList.remove("invalid");
        visaNumberInput.classList.add("valid");

        const anotherButton = document.getElementById("btnAnotherSearch");
        if (anotherButton) {
            anotherButton.addEventListener("click", resetSearchView);
        }
    }

    visaNumberInput.addEventListener("input", validateVisaNumber);
    verificationCodeInput.addEventListener("input", function () {
        if (verificationCodeInput.value.trim() === "") {
            clearVerificationCodeValidation();
            return;
        }
        if (verificationCodeInput.value.trim().toUpperCase() === generatedCaptchaText) {
            clearVerificationCodeValidation();
        }
    });

    const existingAnotherButton = document.getElementById("btnAnotherSearch");
    if (existingAnotherButton) {
        existingAnotherButton.addEventListener("click", resetSearchView);
    }

    visaForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        if (!validateVisaNumber()) {
            return;
        }
        if (!validateVerificationCode()) {
            return;
        }

        const query = new URLSearchParams({
            visaNumber: visaNumberInput.value.trim(),
            ajax: '1',
        });
        const response = await fetch(`${visaForm.action}?${query}`, {
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
        });

        if (!response.ok) {
            setVisaNumberValidity(false, 'Visa number not found');
            return;
        }

        const data = await response.json();
        if (data.found) {
            renderVisaResult(data.visa);
        } else {
            setVisaNumberValidity(false, data.error || 'Visa number not found');
        }
    });
});
