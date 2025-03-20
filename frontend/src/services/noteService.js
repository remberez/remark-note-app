import { api } from ".";

class NoteService {
    static async fetchMyNotes() {
        try {
            const response = await api.get("/notes/my");
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }    
}

export default NoteService;