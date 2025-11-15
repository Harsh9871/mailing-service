import { sendMailService } from "../services/mail.service.js";

export async function sendMail(req, res) {
    try {
        const { to, subject, text, html, smtp } = req.body;

        const result = await sendMailService({ to, subject, text, html, smtp });

        res.json({ success: true, messageId: result.messageId });
    } catch (error) {
        console.error(error);
        res.status(500).json({ success: false, error: error.message });
    }
}
