import React, { useEffect, useState } from 'react';
import { Container, Typography, CircularProgress } from '@mui/material';
import api from '../api';
import AttackLogTable from '../components/AttackLogsTable';
import AlertBanner from '../components/AlertBanner';

const Logs = () => {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const response = await api.get('/logs');
        setLogs(response.data);
      } catch (error) {
        console.error('Error fetching logs:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchLogs();
  }, []);

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Attack Logs
      </Typography>
      {loading ? (
        <CircularProgress />
      ) : logs.length > 0 ? (
        <>
          <AlertBanner message={`Detected ${logs.length} suspicious requests.`} severity="warning" />
          <AttackLogTable logs={logs} />
        </>
      ) : (
        <Typography>No attacks detected yet.</Typography>
      )}
    </Container>
  );
};

export default Logs;
