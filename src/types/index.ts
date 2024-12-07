export interface ChatHistoryItem {
  category: string;
  question: string;
  timestamp: Date;
}

export interface MenuItem {
  icon: React.ComponentType;
  text: string;
  onClick?: () => void;
}