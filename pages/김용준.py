import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';

export default function App() {
  // 과목 선택 상태 (기본값: 국어)
  const [selectedSubject, setSelectedSubject] = useState('국어');
  
  // 과목별 남은 일수 데이터 (예시)
  const assignmentDays = {
    '국어': 8,  // 7일 이상 남음 (잔잔함)
    '수학': 4,  // 3~6일 남음 (조금 셈)
    '영어': 1,  // 1~2일 남음 (매우 거침)
  };

  // 남은 일수에 따라 다른 불꽃 이미지나 스타일을 반환하는 함수
  const getFlameEffect = (days) => {
    if (days >= 7) {
      return { text: "🔥 잔잔한 불꽃 (여유 있음)", color: "#FFCC00", scale: 1.0 };
    } else if (days >= 3) {
      return { text: "🔥🔥 거세지는 불꽃 (준비 필요!)", color: "#FF6600", scale: 1.5 };
    } else {
      return { text: "💥💥💥 폭발하는 불꽃 (당장 하세요!)", color: "#FF0000", scale: 2.3 };
    }
  };

  const currentDays = assignmentDays[selectedSubject];
  const flame = getFlameEffect(currentDays);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>수행평가 알리미</Text>
      
      {/* 과목 선택 버튼 */}
      <View style={styles.tabContainer}>
        {['국어', '수학', '영어'].map((subject) => (
          <TouchableOpacity 
            key={subject} 
            style={[styles.tab, selectedSubject === subject && styles.activeTab]}
            onPress={() => setSelectedSubject(subject)}
          >
            <Text style={styles.tabText}>{subject}</Text>
          </TouchableOpacity>
        ))}
      </View>

      {/* 정보 표시 영역 */}
      <View style={styles.infoBox}>
        <Text style={styles.subjectText}>{selectedSubject} 수행평가</Text>
        <Text style={styles.ddayText}>D-{currentDays}</Text>
        
        {/* 불꽃 시각 효과 영역 */}
        <View style={[
          styles.flameCircle, 
          { backgroundColor: flame.color, transform: [{ scale: flame.scale }] }
        ]}>
          {/* 실제 앱에서는 여기에 크기별 불꽃 GIF나 애니메이션 lottie 파일을 넣으면 됩니다 */}
        </View>
        
        <Text style={styles.statusText}>{flame.text}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#121212', padding: 20, justifyContent: 'center' },
  title: { fontSize: 28, color: '#fff', fontWeight: 'bold', textAlign: 'center', marginBottom: 30 },
  tabContainer: { flexDirection: 'row', justifyContent: 'space-around', marginBottom: 40 },
  tab: { padding: 12, borderRadius: 8, backgroundColor: '#333', width: '25%', alignItems: 'center' },
  activeTab: { backgroundColor: '#ff4757' },
  tabText: { color: '#fff', fontWeight: 'bold' },
  infoBox: { alignItems: 'center', backgroundColor: '#1e1e1e', padding: 30, borderRadius: 16 },
  subjectText: { fontSize: 22, color: '#aaa', marginBottom: 10 },
  ddayText: { fontSize: 40, color: '#fff', fontWeight: 'bold', marginBottom: 30 },
  flameCircle: { width: 60, height: 60, borderRadius: 30, marginBottom: 40, justifyContent: 'center', alignItems: 'center' },
  statusText: { fontSize: 18, color: '#fff', marginTop: 20, fontWeight: 'bold' }
});
