import { Navigate, Route, Routes } from "react-router-dom";
import FloatingShape from "./components/FloatingShape";
import Header from './components/Header';
import Footer from './components/Footer';

import SignUpPage from "./pages/SignUpPage";
import LoginPage from "./pages/LoginPage";
import EmailVerificationPage from "./pages/EmailVerificationPage";
import DashboardPage from "./pages/DashboardPage";
import ForgotPasswordPage from "./pages/ForgotPasswordPage";
import ResetPasswordPage from "./pages/ResetPasswordPage";

import AdminSignUpPage from "./pages/AdminSignUpPage";
import AdminLoginPage from "./pages/AdminLoginPage"
import AdminOTPVerificationPage from "./pages/AdminOTPVerificationPage";
import AdminDash from "./pages/AdminDash";
import Landing from './pages/Landing';
import KnowledgePage from './pages/KnowledgePage';
import DataManagementPage from './pages/DatamanagemnentPage';
import Mentorship from './pages/Mentorship'; // Import Mentorship page
import Contact from './pages/Contact';

import { Toaster } from "react-hot-toast";

function App() {
  return (
 <>
      <Routes>
      <Route path='/' element ={<Landing></Landing>} />
        <Route path="/dash" element={<DashboardPage />} />
        <Route path="/signup" element={<SignUpPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/verify-email" element={<EmailVerificationPage />} />
        <Route path="/forgot-password" element={<ForgotPasswordPage />} />
        <Route path="/reset-password/:token" element={<ResetPasswordPage />} />
        <Route path="/admin/signup" element={<AdminSignUpPage />} />
        <Route path="/admin/login" element={<AdminLoginPage />} />
        <Route path="/admin/verify-otp" element={<AdminOTPVerificationPage />} />
        <Route path="/admin/dash" element={<AdminDash />} />
        {/* Catch-all route */}
        <Route path="/contact" element={<><Header /><Contact /><Footer /></>} />
        <Route path="/mentorship" element={<><Header /><Mentorship /><Footer /></>} />
        
        <Route path="/knowledge-hub" element={<KnowledgePage></KnowledgePage>} />
        <Route path="/datamanagement" element={<DataManagementPage></DataManagementPage>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
      <Toaster />
  </>
  );
}

export default App;
