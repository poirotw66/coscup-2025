#!/usr/bin/env python3
"""
COSCUP 詳細資料提取器
從 coscup_detail.json 提取中文 title 和 description 並儲存為 CSV
"""

import json
import csv
import re
from datetime import datetime


def clean_text(text):
    """清理文字內容，移除多餘的換行符和空白"""
    if not text:
        return ""
    
    # 移除 \r\n 並替換為空格
    text = text.replace('\r\n', ' ')
    # 移除多餘的空白
    text = re.sub(r'\s+', ' ', text)
    # 移除首尾空白
    text = text.strip()
    
    return text


def extract_coscup_data(json_file_path, csv_file_path=None):
    """
    從 COSCUP JSON 檔案中提取資料並儲存為 CSV
    
    Args:
        json_file_path (str): JSON 檔案路徑
        csv_file_path (str): CSV 檔案輸出路徑，如果不指定則自動生成
    
    Returns:
        str: 輸出的 CSV 檔案路徑
    """
    
    # 如果沒有指定 CSV 檔案路徑，則自動生成
    if not csv_file_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file_path = f"coscup_sessions_{timestamp}.csv"
    
    try:
        # 讀取 JSON 檔案
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"成功讀取 JSON 檔案: {json_file_path}")
        
        # 檢查資料結構
        if not isinstance(data, dict) or 'sessions' not in data:
            print("❌ JSON 檔案格式不正確，找不到 'sessions' 欄位")
            return None
        
        sessions = data['sessions']
        extracted_data = []
        
        # 處理每個 session
        for i, session in enumerate(sessions):
            try:
                # 初始化資料行
                row_data = {
                    'session_id': '',
                    'uri': '',
                    'title': '',
                    'description': '',
                    'language': '',
                    'speakers': '',
                    'start_time': '',
                    'end_time': '',
                    'room': '',
                    'type': '',
                    'tags': ''
                }
                
                # 如果 session 只有 uri，跳過
                if isinstance(session, dict) and len(session) == 1 and 'uri' in session:
                    print(f"跳過只有 URI 的 session: {session.get('uri', '')}")
                    continue
                
                # 提取基本資料
                if isinstance(session, dict):
                    row_data['session_id'] = session.get('id', '')
                    row_data['uri'] = session.get('uri', '')
                    row_data['language'] = session.get('language', '')
                    row_data['start_time'] = session.get('start', '')
                    row_data['end_time'] = session.get('end', '')
                    row_data['room'] = session.get('room', '')
                    row_data['type'] = session.get('type', '')
                    
                    # 處理 speakers
                    if 'speakers' in session and isinstance(session['speakers'], list):
                        row_data['speakers'] = ', '.join(session['speakers'])
                    
                    # 處理 tags
                    if 'tags' in session and isinstance(session['tags'], list):
                        row_data['tags'] = ', '.join(session['tags'])
                    
                    # 提取中文 title 和 description
                    if 'zh' in session and isinstance(session['zh'], dict):
                        zh_data = session['zh']
                        
                        # 提取 title
                        if 'title' in zh_data:
                            row_data['title'] = clean_text(zh_data['title'])
                        
                        # 提取 description
                        if 'description' in zh_data:
                            row_data['description'] = clean_text(zh_data['description'])
                    
                    # 如果沒有中文資料，檢查英文資料
                    elif 'en' in session and isinstance(session['en'], dict):
                        en_data = session['en']
                        
                        # 提取英文 title 和 description 作為備用
                        if 'title' in en_data:
                            row_data['title'] = clean_text(en_data['title'])
                        
                        if 'description' in en_data:
                            row_data['description'] = clean_text(en_data['description'])
                    
                    # 只有當有 title 或 description 時才加入
                    if row_data['title'] or row_data['description']:
                        extracted_data.append(row_data)
                        print(f"✅ 提取第 {i+1} 個 session: {row_data['title'][:50]}...")
                
            except Exception as e:
                print(f"處理第 {i+1} 個 session 時出錯: {e}")
                continue
        
        # 儲存為 CSV
        if extracted_data:
            fieldnames = [
                'session_id',
                'uri', 
                'title',
                'description',
                'language',
                'speakers',
                'start_time',
                'end_time',
                'room',
                'type',
                'tags'
            ]
            
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(extracted_data)
            
            print(f"\n✅ 成功提取 {len(extracted_data)} 筆資料")
            print(f"📁 CSV 檔案已儲存至: {csv_file_path}")
            
            # 顯示前幾筆資料預覽
            print(f"\n📋 資料預覽 (前3筆):")
            for i, item in enumerate(extracted_data[:3]):
                print(f"  {i+1}. 標題: {item['title'][:80]}...")
                print(f"     描述: {item['description'][:100]}...")
                print(f"     URI: {item['uri']}")
                print()
            
            return csv_file_path
        
        else:
            print("❌ 沒有找到任何有效的 session 資料")
            return None
            
    except FileNotFoundError:
        print(f"❌ 找不到檔案: {json_file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 檔案格式錯誤: {e}")
        return None
    except Exception as e:
        print(f"❌ 處理檔案時發生錯誤: {e}")
        return None


def main():
    """主函數"""
    print("🚀 開始提取 COSCUP 議程資料...")
    
    # 設定檔案路徑
    json_file = "coscup_detail.json"
    csv_file = "coscup_sessions_extracted.csv"
    
    # 執行提取
    result = extract_coscup_data(json_file, csv_file)
    
    if result:
        print(f"\n🎉 提取完成！")
        print(f"📊 結果檔案: {result}")
    else:
        print(f"\n❌ 提取失敗")


if __name__ == "__main__":
    main()
