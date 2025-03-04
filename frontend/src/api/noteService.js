import $api from "./api";

class NoteService {
    static async fetchMyNotes() {
        try {
            const response = await $api.get("/notes/my");
            return response.data;
        } catch (error) {
            console.error("Произошла ошибка при получении заметок", error);
        }
    }
}

export default NoteService;
