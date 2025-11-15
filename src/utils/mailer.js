import nodemailer from "nodemailer";
import dotenv from "dotenv";
dotenv.config();

export function mailTransporter(customConfig = {}) {
    const transporter = nodemailer.createTransport({
        host: customConfig.host || process.env.DEFAULT_MAIL_HOST,
        port: customConfig.port || process.env.DEFAULT_MAIL_PORT,
        secure: false, // change to true if using port 465
        auth: {
            user: customConfig.user || process.env.DEFAULT_MAIL_USER,
            pass: customConfig.pass || process.env.DEFAULT_MAIL_PASS
        }
    });

    return transporter;
}
