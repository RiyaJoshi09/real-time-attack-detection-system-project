import React, { useEffect, useState } from 'react';
import { Container, Typography, Box } from '@mui/material';
import { io } from 'socket.io-client';
import AttackLogsTable from '../components/AttackLogsTable';
import AlertBanner from '../components/AlertBanner';
import { getAttackLogs } from '../api';

const socket = io(process.env.REACT_APP_API_URL || 'http://localhost:5000');

const Dashboard = () => {
  const [logs, setLogs] = useState([]);
  const [latestAttack, setLatestAttack] = useState(null);
  const [alertOpen, setAlertOpen] = useState(false);

  useEffect(() => {
    // Initial fetch
    const fetchLogs = async () => {
      try {
        const response = await getAttackLogs();
        setLogs(response.data.reverse());
      } catch (error) {
        console.error('Error fetching logs:', error);
      }
    };

    fetchLogs();

    // Listen for real-time attack alerts
    socket.on('attack_alert', (log) => {
      setLogs((prevLogs) => [log, ...prevLogs]);
      setLatestAttack(log);
      setAlertOpen(true);
      setTimeout(() => setAlertOpen(false), 5000);
    });

    return () => {
      socket.off('attack_alert');
    };
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Box mt={2}>
        <AlertBanner log={latestAttack} open={alertOpen} />
      </Box>
      
      <Box mt={3}>
        <AttackLogsTable logs={logs} />
      </Box>
    </Container>
  );
};

export default Dashboard;
