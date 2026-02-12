import React from 'react';
import { useAuth } from '../context/AuthContext';
import { FaUser, FaEnvelope, FaPhone, FaEdit } from 'react-icons/fa';

const Profile: React.FC = () => {
  const { user } = useAuth();

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-8">
          <div className="card shadow-sm border-0">
            <div className="card-body p-5">
              {/* Header */}
              <div className="text-center mb-4">
                <div className="d-inline-flex align-items-center justify-content-center bg-primary text-white rounded-circle mb-3" 
                     style={{ width: '100px', height: '100px', fontSize: '2.5rem' }}>
                  <FaUser />
                </div>
                <h2 className="fw-bold mb-1">{user?.firstName} {user?.lastName}</h2>
                <p className="text-muted">{user?.email}</p>
              </div>

              {/* Profile Information */}
              <div className="mb-4">
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h5 className="fw-bold mb-0">Profile Information</h5>
                  <button className="btn btn-outline-primary btn-sm">
                    <FaEdit className="me-2" />
                    Edit Profile
                  </button>
                </div>
                <hr />
              </div>

              {/* Details */}
              <div className="row g-4">
                <div className="col-md-6">
                  <div className="d-flex align-items-start gap-3">
                    <div className="bg-light rounded p-3">
                      <FaUser className="text-primary" />
                    </div>
                    <div>
                      <div className="small text-muted">First Name</div>
                      <div className="fw-semibold">{user?.firstName}</div>
                    </div>
                  </div>
                </div>

                <div className="col-md-6">
                  <div className="d-flex align-items-start gap-3">
                    <div className="bg-light rounded p-3">
                      <FaUser className="text-primary" />
                    </div>
                    <div>
                      <div className="small text-muted">Last Name</div>
                      <div className="fw-semibold">{user?.lastName}</div>
                    </div>
                  </div>
                </div>

                <div className="col-md-6">
                  <div className="d-flex align-items-start gap-3">
                    <div className="bg-light rounded p-3">
                      <FaEnvelope className="text-primary" />
                    </div>
                    <div>
                      <div className="small text-muted">Email Address</div>
                      <div className="fw-semibold">{user?.email}</div>
                    </div>
                  </div>
                </div>

                <div className="col-md-6">
                  <div className="d-flex align-items-start gap-3">
                    <div className="bg-light rounded p-3">
                      <FaPhone className="text-primary" />
                    </div>
                    <div>
                      <div className="small text-muted">Phone Number</div>
                      <div className="fw-semibold">{user?.phone || 'Not provided'}</div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Account Actions */}
              <div className="mt-5">
                <h5 className="fw-bold mb-3">Account Settings</h5>
                <hr />
                <div className="d-grid gap-2">
                  <button className="btn btn-outline-secondary text-start">
                    Change Password
                  </button>
                  <button className="btn btn-outline-secondary text-start">
                    Notification Preferences
                  </button>
                  <button className="btn btn-outline-danger text-start">
                    Delete Account
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
