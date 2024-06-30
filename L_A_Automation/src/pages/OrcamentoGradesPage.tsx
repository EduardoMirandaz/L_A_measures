import React from 'react';

import styles from './OrcamentoGradesPage.module.css'; 

export function OrcamentoGradesPage() {
    return (
        <div className={styles.breadcrumb}>
            <span className={styles.home}>Página Principal</span>
            <span> / </span>
            <span className={styles.Produto}>Produto</span>
        </div>
    )
}

export default OrcamentoGradesPage;