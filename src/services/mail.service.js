import { mailTransporter } from "../utils/mailer.js";

export async function sendMailService({ to, subject, text, html, smtp }) {
    const transporter = mailTransporter(smtp); 

    const mailOptions = {
        from: smtp?.from || process.env.DEFAULT_MAIL_FROM,
        to,
        subject,
        text,
        html
    };

    return await transporter.sendMail(mailOptions);
}
