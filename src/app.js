import express from "express";
import mailRoutes from "./routes/mail.routes.js";
import rateLimit from "express-rate-limit";

const app = express();
app.use(express.static("public"));

const PORT = process.env.PORT || 3100;

app.use(express.json());

// Rate limiting configuration
const createRateLimiter = (maxRequests, windowMs) => {
  return rateLimit({
    windowMs: windowMs,
    max: maxRequests,
    message: {
      success: false,
      error: `Too many requests, please try again later.`
    },
    standardHeaders: true,
    legacyHeaders: false,
    keyGenerator: (req) => {
      // Use IP address as the key for rate limiting
      return req.ip;
    },
    skip: (req) => {
      // Skip rate limiting for localhost and trusted IPs
      const clientIP = req.ip;
      const trustedIPs = process.env.TRUSTED_IPS ? 
        process.env.TRUSTED_IPS.split(',') : [];
      
      const isLocalhost = clientIP === '127.0.0.1' || 
                         clientIP === '::1' || 
                         clientIP === '::ffff:127.0.0.1';
      
      const isTrustedIP = trustedIPs.includes(clientIP);
      
      return isLocalhost || isTrustedIP;
    }
  });
};

// Apply rate limiting: 5 requests per minute for untrusted IPs
const emailRateLimiter = createRateLimiter(5, 1 * 60 * 1000); // 5 requests per minute

// Apply rate limiting to mail routes
app.use("/api/mail", emailRateLimiter, mailRoutes);

app.listen(PORT, () => {
    console.log(`Mailing microservice running on port ${PORT}`);
    console.log(`Rate limiting: 5 emails/minute for untrusted IPs`);
    console.log(`No rate limiting for: localhost${process.env.TRUSTED_IPS ? ` and ${process.env.TRUSTED_IPS.split(',').length} trusted IPs` : ''}`);
});